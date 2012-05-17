var times = 1000;
while(times--) {
  var array = []
  while(array.push(Math.floor((Math.random()*100000)+1)) < 1000000)
  var start = Date.now()
  array.sort(function(a,b){return a-b})
  var end = Date.now()
  console.log("Elapsed time: %d microseconds", (end - start) * 1000)
}
