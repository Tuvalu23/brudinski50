;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Team JBEE-Mini :: Ben Rudinski, Endrit Idrizi
;SoftDev pd5
;K27 - Basic functions in JavaScript
;2025-01-06m

;Scheme antecedents for JavaScript work


;factorial:
(define fact (lambda (n)
    (if (= n 0)
        1
        (* n (fact (- n 1))))))

;TEST CALLS
(fact 1)
(fact 2) ;"...should be  2"
(fact 3) ;"...should be  6"
(fact 4) ;"...should be  24"
(fact 5) ;"...should be  120"


;-----------------------------------------------------------------


;fib:
;<your team's fib(n) implementation>

(define fib(lambda (n)
             (cond
               ((= n 0) 0)
               ((= n 1) 1)
               (else (+ (fib (- n 1)) (fib (- n 2)))))))

;TEST CALLS
(fib 0) ;"...should be  0"
(fib 1) ;"...should be  1"
(fib 2) ;"...should be  1"
(fib 3) ;"...should be  2"
(fib 4) ;"...should be  3"

;=================================================================