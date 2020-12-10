// Rosalind rna

use aoclib;
use std::io;

fn main() -> io::Result<()> {
    let lines = aoclib::read_file_string(&"rosalind_rna.txt")?;

    let rna = lines.replace("T", "U");

    println!("{}", rna);

    Ok(())
}
