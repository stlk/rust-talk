#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
    }
}

mod buffer; // a small buffer struct + impl, not shown
use buffer::Buffer;

#[no_mangle]
pub extern "C" fn fast_blank(buf: Buffer) -> bool {
  buf.as_slice().chars().all(|c| c.is_whitespace())
}

#[no_mangle]
pub extern "C" fn fib(n: u32) -> u32 {
    if n <= 1 {
        return n;
    } else {
        return fib(n-1) + fib(n-2);
    }
}
