use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn main() {
    const FILE_PATH: &str = "./input.txt";
    let lines: Vec<String> = lines_from_file(FILE_PATH);
    let mut sum: i32 = 0;
    let mut front: i32; 
    let mut back: i32;
    let mut value: i32;
    for i in 0..lines.len() {
        front = -1;
        back = 0;
        for character in lines[i].chars(){
            value = occurs_within(character);
            if value != -1 {
                front = if front == -1 {value} else {front};
                back = value;
            }
        }
        // println!("{}{}", front,back);
        sum += front*10 + back;
    }
    println!("{}", sum);
    // println!("{}", contents);
    // println!("With text:\n{contents}");

}

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn occurs_within(character: char) -> i32{
    const DIGITS: &str = "0123456789";
    let mut val: i32 = 0;
    for d in DIGITS.chars() {
        if character == d {
            return val;
        }
        val += 1;
    }
    -1
}

// fn print_type_of<T>(_: &T) {
//     println!("{}", std::any::type_name::<T>())
// }