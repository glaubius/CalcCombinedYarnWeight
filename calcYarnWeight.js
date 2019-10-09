

// Change label text

$('.dropdown-item').on('click', function(){
  var btnObj = $(this).parent().siblings('button');
  $(btnObj).text($(this).text());
  $(btnObj).val($(this).text());
});

// Calculate button actions
$(".calculate-btn").click(function(){

  var yarnnumber = 0;

  //alert("Calculate button has been pressed!");
  var y1weight = $("#yarn1weight").val();
  var y1wlabel = $(".btn-y1weight-label").val();
  var y1length = $("#yarn1length").val();
  var y1llabel = $(".btn-y1length-label").val();
  var y2weight = $("#yarn2weight").val();
  var y2wlabel = $(".btn-y2weight-label").val();
  var y2length = $("#yarn2length").val();
  var y2llabel = $(".btn-y2length-label").val();
  var y3weight = $("#yarn3weight").val();
  var y3wlabel = $(".btn-y3weight-label").val();
  var y3length = $("#yarn3length").val();
  var y3llabel = $(".btn-y3length-label").val();

  //Alert user if not both weight and length are include for a yarn
  if (y1weight != "") {
    if (y1length === "") {
      alert("Enter a length for yarn 1");
    } else {
      yarnnumber++;
    }
  } else {
    if (y1length != ""){
      alert("Enter a weight for yarn 1");
    }
  }

  if (y2weight != "") {
    if (y2length === "") {
      alert("Enter a length for yarn 2");
    } else {
      yarnnumber++;
    }
  } else {
    if (y2length != ""){
      alert("Enter a weight for yarn 2");
    }
  }

  if (y3weight != "") {
    if (y3length === "") {
      alert("Enter a length for yarn 3");
    } else {
      yarnnumber++;
    }
  } else {
    if (y3length != ""){
      alert("Enter a weight for yarn 3");
    }
  }


  // Convert ounces and yards to grams and meters
  if (y1wlabel === "ounces"){
    var newY1w = convertOzToGr(y1weight);
    y1weight = newY1w;
  }
  if (y1llabel === "yards"){
    var newY1l = convertYdToMeters(y1length);
    y1length = newY1l;
  }
  if (y2wlabel === "ounces"){
    var newY2w = convertOzToGr(y2weight);
    y2weight = newY2w;
  }
  if (y2llabel === "yards"){
    var newY2l = convertYdToMeters(y2length);
    y2length = newY2l;
  }
  if (y3wlabel === "ounces"){
    var newY3w = convertOzToGr(y3weight);
    y3weight = newY3w;
  }
  if (y3llabel === "yards"){
    var newY3l = convertYdToMeters(y3length);
    y3length = newY3l;
  }

  var combinedWperM = 0;
  // Calculate weight per meter
  if (yarnnumber === 0 | yarnnumber === 1){
    alert("Enter information for at least 2 yarns");
  } else if (yarnnumber === 2){
    var y1WperM = y1weight / y1length;
    var y2WperM = y2weight / y2length;
    combinedWperM = y1WperM + y2WperM;
  } else {
    var y1WperM = y1weight / y1length;
    var y2WperM = y2weight / y2length;
    var y3WperM = y3weight / y3length;
    combinedWperM = y1WperM + y2WperM + y3WperM;
  }

  var meterPer100gr = 100 / combinedWperM;

  var stndWeight = "";
  if (meterPer100gr >= 0 & meterPer100gr < 50){
    stndWeight = "7 - Jumbo, Roving";
  } else if (meterPer100gr >= 50 & meterPer100gr < 90){
    stndWeight = "6 - Super Bulky";
  } else if (meterPer100gr >= 90 & meterPer100gr < 110){
    stndWeight = "5 - Bulky, Chunky, 14 ply";
  } else if (meterPer100gr >= 110 & meterPer100gr < 240){
    stndWeight = "4 - Medium, Worsted, Aran, 10/12 ply";
  } else if (meterPer100gr >= 240 & meterPer100gr < 300){
    stndWeight = "3 - Light, DK, Light Worsted, 8 ply";
  } else if (meterPer100gr >= 300 & meterPer100gr < 400){
    stndWeight = "2 - Fine, Sport, 4 ply";
  } else if (meterPer100gr >= 400 & meterPer100gr < 600){
    stndWeight = "1 - Super Fine, Fingering, 3 ply";
  } else if (meterPer100gr >= 600 & meterPer100gr < 10000){
    stndWeight = "0 - Lace, Cobweb";
  }

  var grMeter = meterPer100gr / 100;
  var gr50Meter = meterPer100gr / 2;
  var gr200Meter = meterPer100gr * 2;

  $("#result-text").text(stndWeight);

  $("#1gr-meter").text(grMeter.toFixed(1));
  $("#1gr-yard").text((grMeter * 1.09361).toFixed(1));
  $("#50gr-meter").text(gr50Meter.toFixed(1));
  $("#50gr-yard").text((gr50Meter * 1.09361).toFixed(1));
  $("#100gr-meter").text(meterPer100gr.toFixed(1));
  $("#100gr-yard").text((meterPer100gr * 1.09361).toFixed(1));
  $("#200gr-meter").text(gr200Meter.toFixed(1));
  $("#200gr-yard").text((gr200Meter * 1.09361).toFixed(1));



});


// Functions

function convertOzToGr(ounces){
  var grams = ounces * 28.3495;
  return grams;
}

function convertYdToMeters(yards){
  var meters = yards * 0.9144;
  return meters;
}
