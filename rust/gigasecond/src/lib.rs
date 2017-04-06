extern crate chrono;
use chrono::*;


pub fn after(date: DateTime<UTC>) -> DateTime<UTC> {
    let gigasecond = Duration::seconds(1000000000);
    return date + gigasecond;
}
