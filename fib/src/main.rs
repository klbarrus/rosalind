// Rosalind fib

use aoclib;
use std::io;

fn ros_fib(n: usize, k: usize) -> usize {
    let mut rabbits: Vec<usize> = Vec::new();
    rabbits.reserve(n + 1);
    rabbits.push(0);
    rabbits.push(1);

    for gen in 2..=n {
        rabbits.push(rabbits[gen - 1] + k * rabbits[gen - 2]);
    }

    rabbits[n]
}

fn main() -> io::Result<()> {
    let lines = aoclib::read_file_string(&"rosalind_fib.txt")?;
    let nums = lines
        .split_whitespace()
        .map(|ch| ch.parse::<usize>().unwrap())
        .collect::<Vec<_>>();
    let res = ros_fib(nums[0], nums[1]);

    println!("{}", res);

    Ok(())
}
