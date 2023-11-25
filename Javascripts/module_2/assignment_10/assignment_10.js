'use strict';

function compare(a, b) {
    return b.votes - a.votes
}

let candidates = [];
let num_candidates = prompt('Please input the number of candidates');

for (let i=0; i<num_candidates; i++) {
    candidates[i] = {
        name: prompt(`Name for candidate ${i}`),
        votes: 0
    }
}

let num_voters = prompt('Please input the number of voters');


for (let j=0; j<num_voters; j++) {
    const name = prompt(`Voter ${j+1}: Who do you vote?`);
    for (let k=0; k<num_candidates; k++) {
        if (candidates[k].name == name ) {
            candidates[k].votes ++;
        }
    }
}

candidates.sort(compare);

console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
console.log('results:');

for (let l=0; l<num_candidates; l++) {
    console.log(`${candidates[l].name }: ${candidates[l].votes} votes`)
}
