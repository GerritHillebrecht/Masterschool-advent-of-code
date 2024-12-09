const fs = require("fs")


// Datei asynchron lesen
//fs.readFile('inputs/day_9_input_disk_map.txt', 'utf8', (err, data) => {
//  if (err) {
//    console.error('Fehler beim Lesen der Datei:', err);
//    return;
//  }
//  console.log('Inhalt der Datei:', data);
//});

function read_data() {
    try {
      return fs.readFileSync('inputs/day_9_input_disk_map.txt', 'utf8');
    } catch (err) {
      console.error('Fehler beim Lesen der Datei:', err);
    }
}


function checksum(blocks) {
    let sum = 0;
    blocks.map(Number).forEach((num, index) => {
        if (!isNaN(num)) {
            sum += num * index;
        }
    });
    return sum;
}

function mapToBlocks(text) {
    let blocks = [];

    let isBlock = true;
    let id = 0;
    text.split('').forEach((char) => {
        if (isBlock) {
            for (let index = 0; index < +char; index++) {
                blocks.push(`${id}`);
            }
            id++;
        } else {
            for (let index = 0; index < +char; index++) {
                blocks.push('.');
            }
        }
        isBlock = !isBlock;
    });

    return blocks;
}

function minifyBlocks(blocks) {
    let arr = blocks;
    let keepMoving = true;

    while (keepMoving) {
        const dotIndex = arr.indexOf('.');

        if (dotIndex === -1) {
            keepMoving = false;
        } else if (dotIndex === arr.length - 1) {
            arr = arr.slice(0, -1);
        } else {
            const last = arr[arr.length - 1];
            if (last !== '.') {
                arr[dotIndex] = last;
            }
            arr = arr.slice(0, -1);
        }
    }

    return arr;
}

const data = read_data();
mappedBlocks = mapToBlocks(data)
minifiedBlocks = minifyBlocks(mappedBlocks)
//checksum = checksum(minifiedBlocks)
console.log(minifiedBlocks)