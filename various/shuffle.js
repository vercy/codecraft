const arr = ['apple', 'banana', 'coconut', 'dragon fruit', 'elderberry', 'fig']

// const naive = arr.sort((a, b) => 0.5 - Math.random())
// console.log(naive)

// const fixed = arr
//     .map((v) => [v, Math.random()])
//     .sort((a, b) => a[1] - b[1])
//     .map((v) => v[0])
// console.log(fixed)

const fisher = (arr) => {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]]
    }
    return arr
}
console.log(fisher(arr))
