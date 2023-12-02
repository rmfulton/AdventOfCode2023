use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
    str::Chars;
};

fn main() {
    const FILE_PATH: &str = "./sample.txt";
    const lines: Vec<String> = lines_from_file(FILE_PATH);
    let mut sum: i32 = 0;
    let mut front: i32; 
    let mut back: i32;
    let mut value: i32;
    for i in 0..lines.len() {
        front = get_first_digit(lines[i]);
        back = get_last_digit(lines[i]);
        value = front*10 + back;
        sum += value;
        println!("{}", value);
    }
    println!("{}", sum);
}

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn get_first_digit(line: String) -> i32 {
    let chars: Chars<'_> = line.chars();
    for currentIndex in 0..chars.len() {
        let res = matches(line, currentIndex);
        if res != -1{
            return res;
        }
    }
    return -1;

}

fn get_last_digit(line: String) -> i32{
    return 0;
}

fn matches(line: string, i: usize) -> i32{
    characters = line.chars();
    const numbers: [&str; 10] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
    const words: [&str; 10] = ["zero","one", "two", "three", "four", "five","six", "seven", "eight", "nine"];
    for j in 0..numbers.len() {
        if line[i] == line[j] {
            return j
        }
        else {
            let w = words[j];
            if (i + w.len() <= characters.len()){
                let mut equal = true;
                for k in 0..w.len() {
                    if w[k] != w[i + k] {
                        equal = false;
                    }
                }
                if equal {
                    return j
                }
            }
        }
    }
    return -1
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