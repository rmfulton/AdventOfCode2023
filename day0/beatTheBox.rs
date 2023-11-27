fn main(){
    println!(probability())
}

fn probability(){
    const n = 0;
    // We have 4 cards at each rank
    let counts: [u8, 13] = [4; 13];
    const DECK_STATES = 1 << 26;
}