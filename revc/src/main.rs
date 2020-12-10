// Rosalind revc

use aoclib;
use std::io;

fn main() -> io::Result<()> {
    let lines = aoclib::read_file_string(&"rosalind_revc.txt")?;

    let revc: String = lines.chars().rev().map(|ch| match ch {
        'A' => 'T',
        'C' => 'G',
        'G' => 'C',
        'T' => 'A',
        _ => ' '
    }).collect::<Vec<_>>().into_iter().collect();

    println!("{}", revc);

    Ok(())
}
