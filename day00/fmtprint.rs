fn main() {
	println!("{} days", 31);
	println!("{} days, {} months", 365, 12);
	println!("{0}, this is {1}. {1}, this is {0}.", "Alice", "Bob");
	println!("{subject} {verb} {object}", subject="the quick brown fox", object="the lazy dog", verb= "jumps over");

	// println!("Base 10:               {}",   69420); // 69420
    // println!("Base 2 (binary):       {:b}", 69420); // 10000111100101100
    // println!("Base 8 (octal):        {:o}", 69420); // 207454
    // println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c
    // println!("Base 16 (hexadecimal): {:X}", 69420); // 10F2C

	//right justify text
	println!("{number:>5}", number=1);
	println!()
}
