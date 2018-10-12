let fib n = 
        let rec loop ct a b = 
                if ct = 0 then a
                else loop (ct - 1) (b) (a+b)
        in loop n 0 1;;

print_endline (string_of_int (fib 10))
