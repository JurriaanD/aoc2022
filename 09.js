// The input
let moves;
// Which line of the input we're at
let step = 0;
// List of the knots we're simulating (each has x, y)
let knots;
// List of colors for drawing the knots
let colors;
// Stack of the previous states of the knots
let history;
// Positions where the tail has been
let positions = new Set();
// Number of knots to simulate
const KNOT_COUNT = 10;

class Move {
    constructor(moveStr) {
        let [dirStr, stepsizeStr] = moveStr.split(" ");
        this.stepSize = parseInt(stepsizeStr);
        this.dir = {
            'L': { x: -1, y: 0 },
            'R': { x: 1, y: 0 },
            'U': { x: 0, y: 1 },
            'D': { x: 0, y: -1 }
        }[dirStr];
    }
}

function preload() {
    loadStrings('09.in', strMoves => {
        moves = strMoves.map(moveStr => new Move(moveStr));
    });
}

function setup() {
    createCanvas(600, 600);
    frameRate(10);

    knots = Array(KNOT_COUNT).fill(null).map(_ => ({ x: 0, y: 0 }));
    colors = [color(0, 255, 0), color(0, 0, 255), 0, 10, 30, 50, 70, 90, 110, 120];
    history = [];
    positions.add(JSON.stringify(knots[KNOT_COUNT - 1]));
}

function draw() {
    background(255);

    // Grid
    strokeWeight(1);
    stroke(150);
    for (let y = 0; y < height; y += 10) {
        line(0, y, width, y);
    }
    for (let x = 0; x < width; x += 10) {
        line(x, 0, x, height);
    }

    // Center (0,0)
    translate(width / 2, height / 2);

    drawKnots();
}

function keyPressed() {
    if (keyCode === RIGHT_ARROW) {
        stepForward();
    } else if (keyCode === LEFT_ARROW) {
        stepBackward();
    } else if (keyCode === ENTER) {
        // Run the entire simulation at once
        while (step < moves.length) {
            stepForward();
        }
        console.log(positions.size);
    }
}

function stepForward() {
    if (step >= moves.length) {
        console.log("The end!");
        return;
    }

    history.push(JSON.parse(JSON.stringify(knots)));

    const move = moves[step++];
    const head = knots[0];

    for (let _ = 0; _ < move.stepSize; _++) {
        head.x += move.dir.x;
        head.y += move.dir.y;
    
        for (let i = 0; i < knots.length - 1; i++) {
            a = knots[i];
            b = knots[i+1];

            dx = a.x - b.x;
            dy = a.y - b.y;

            if (abs(dx) + abs(dy) >= 3) {
                // Diagonal
                b.x += Math.sign(dx);
                b.y += Math.sign(dy);
            } else if (abs(dx) == 2) {
                b.x += Math.sign(dx);
            } else if (abs(dy) == 2) {
                b.y += Math.sign(dy);
            }
        }
    
        positions.add(JSON.stringify(knots[KNOT_COUNT - 1]));
    }
}

function stepBackward() {
    if (step == 0) {
        console.log("This is the start!");
        return;
    }
    step--;
    knots = history.pop();
}

function drawKnots() {
    //const center = {x: knots[0].x, y: knots[0].y};
    const center = { x: 0, y: 0 };

    strokeWeight(10);

    for (let i = 0; i < knots.length; i++) {
        const knot = knots[i];
        stroke(colors[i]);
        point(10*(knot.x - center.x), 10*(knot.y - center.y));
    }
}