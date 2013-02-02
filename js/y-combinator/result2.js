// Ymem takes a functional and an (optional)
// cache of answers.

// It returns the fixed point of the functional
// that caches intermediate results.
  
function Ymem(F, cache) {
 if (!cache)
  cache = {} ; // Create a new cache.
 return function(arg) {
  if (cache[arg])
   return cache[arg] ; // Answer in cache.
  var answer = (F(function(n){
   return (Ymem(F,cache))(n);
  }))(arg) ; // Compute the answer.
  cache[arg] = answer ; // Cache the answer.
  return answer ;
 } ;
}

var fib = Ymem(function (g) { return (function (n) {
 if (n == 0) return 0 ;
 if (n == 1) return 1 ;
 return g(n-1) + g(n-2) ;
}) ; }) ;

document.getElementById("result2").innerHTML =
 fib(100);
