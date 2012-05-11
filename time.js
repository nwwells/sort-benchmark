var times = 100;
while(times--) {
  var array = []
  while(array.push(Math.floor((Math.random()*100000)+1)) < 10000)
  var start = Date.now()
  array.sort()
  var end = Date.now()
  console.log("Elapsed time: %d milliseconds", end - start)
}
