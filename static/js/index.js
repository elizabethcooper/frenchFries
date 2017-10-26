function httpGet(theUrl)
{
    console.log(theUrl);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, true);
    xmlHttp.send();
    console.log("testing");
    console.log(xmlHttp)
    var text = JSON.parse(xmlHttp.responseText);
    var dateTime = text.date;
    var date = dateTime.substring(5,7) + "-" + dateTime.substring(8,10) + "-" + dateTime.substring(0,4);
    var time = dateTime.substring(11, 18);
    dateTime = date + " " + time;
    return dateTime;
}