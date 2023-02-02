clock = () => {
  let times = new Date();
  dates = times.toLocaleDateString();
  a = times.getHours() + ":" + times.getMinutes() + ":" + times.getSeconds();
  document.getElementById("times").innerHTML = a + "  on  " + dates;
  console.log(a);
};

setInterval(clock, 1000);

clocks = () => {
  let times = new Date();
  times.setDate(times.getDate() + 7); // set date to 7 days in the future
  a = times.getHours() + ":" + times.getMinutes() + ":" + times.getSeconds();
  document.getElementById("time").innerHTML = a + "  on  " + times.toLocaleDateString();
};

setInterval(clocks, 1000);
