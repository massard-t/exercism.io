pub fn raindrops(drops: i32) ->  String {
    let mut my_string = "".to_owned();
    let mut has_changed = false;
    if drops%3 == 0 {
        my_string.push_str("Pling");
        has_changed = true;
    }
    if drops%5 == 0 {
        my_string.push_str("Plang");
        has_changed = true;
    }
    if drops%7 == 0 {
        my_string.push_str("Plong");
        has_changed = true;
    }
    if has_changed == false {
        my_string = drops.to_string();
    }
    my_string
}
