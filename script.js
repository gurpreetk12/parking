var firebaseConfig = {
    apiKey: "AIzaSyCtLv9WjKfJdOM6LQ-VBP9uOWCPdklBr0E",
    authDomain: "parkit-f33d5.firebaseapp.com",
    databaseURL: "https://parkit-f33d5-default-rtdb.firebaseio.com",
    projectId: "parkit-f33d5",
    storageBucket: "parkit-f33d5.appspot.com",
    messagingSenderId: "116374492230",
    appId: "1:116374492230:web:1e4dd0e5d69ab519b26647",
    measurementId: "G-8T7JPSE3ET"
  };
  
  // // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  let slots
  var dbRef = firebase.database().ref("nodemcu1")
  dbRef.once("value", function (snapshot) {
    var data = snapshot;
    slots = data.val();
    console.log(data.val());
    if(slots.slot1=="0")
    {
      document.getElementById("slot1").innerHTML="Unavailable"
    }
    else
    {
      document.getElementById("slot1").innerHTML="Available" 
    }
    if(slots.slot2=="0")
    {
      document.getElementById("slot2").innerHTML="Unavailable"
    }
    else
    {
      document.getElementById("slot2").innerHTML="Available" 
    }
    if(slots.slot3=="0")
    {
      document.getElementById("slot3").innerHTML="Unavailable"
    }
    else
    {
      document.getElementById("slot3").innerHTML="Available" 
    }
    if(slots.slot4=="0")
    {
      document.getElementById("slot4").innerHTML="Unavailable"
    }
    else
    {
      document.getElementById("slot4").innerHTML="Available" 
    }
  })
