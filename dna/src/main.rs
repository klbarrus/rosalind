// Rosalind dna

use aoclib;
use std::io;

fn base_count(
    (mut a, mut c, mut g, mut t): (usize, usize, usize, usize),
    ch: char,
) -> (usize, usize, usize, usize) {
    match ch {
        'A' => a = a + 1,
        'C' => c = c + 1,
        'G' => g = g + 1,
        'T' => t = t + 1,
        _ => (),
    }

    (a, c, g, t)
}

fn main() -> io::Result<()> {
    let lines = aoclib::read_file_string(&"rosalind_dna.txt")?;

    let count = lines
        .chars()
        .fold((0, 0, 0, 0), |acc, x| base_count(acc, x));

    println!("{} {} {} {}", count.0, count.1, count.2, count.3);

    Ok(())
}
