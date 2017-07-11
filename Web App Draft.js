<!doctype html>
<html lang="en">
<head>

<title>Wave Web App</title>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
<link rel="stylesheet" type="text/css" href="style.css">

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.min.js"></script>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js"></script>
<script type="text/javascript">

/*JavaScript starts here*/

var correctCards = 0;
$( init );

function init() {

  //Hide the submit opttion

  $('#submitBox').hide();
  

  // Reset the game
  correctCards = 0;
  $('#cardPile').html( '' );
  $('#cardSlots').html( '' );

  // Create the pile of shuffled cards
  var numbers = [ 1, 2, 3, 4 ];
  numbers.sort( function() { return Math.random() - .5 } );

  for ( var i=0; i<4; i++ ) {
    $('<div>' + numbers[i] + '</div>').data( 'number', numbers[i] ).attr( 'id', 'card'+numbers[i] ).appendTo( '#cardPile' ).draggable( {
      containment: '#content',
      stack: '#cardPile div',
      cursor: 'move',
      revert: true
    } );
  }

  // Create the card slots
  var words = [ 'X', 'X', 'X', 'X' ];
  for ( var i=1; i<=4; i++ ) {
    $('<div>' + words[i-1] + '</div>').data( 'number', i ).appendTo( '#cardSlots' ).droppable( {
      accept: '#cardPile div',
      hoverClass: 'hovered',
      drop: handleCardDrop
    } );
  }

}

function handleCardDrop( event, ui ) {
  var slotNumber = $(this).data( 'number' );
  var cardNumber = ui.draggable.data( 'number' );

  // If the card was dropped to the correct slot,
  // change the card colour, position it directly
  // on top of the slot

  if ( slotNumber != cardNumber ) {
    ui.draggable.addClass( 'correct' );
    
    ui.draggable.position( { of: $(this), my: 'left top', at: 'left top' } );
    ui.draggable.draggable( 'option', 'revert', false );
    correctCards++;
  } 

  
  else{
    ui.draggable.addClass( 'correct' );
    
    ui.draggable.position( { of: $(this), my: 'left top', at: 'left top' } );
    ui.draggable.draggable( 'option', 'revert', false );
    correctCards++;
  }
  
  
  // If all the cards have been placed correctly then display a message
  // and reset the cards for another go


  if ( correctCards == 4 ) {      //Needs to be replaced with submit button and form fill out
    $('#submitBox').show();
    

   
  }

}

</script> 

 /*End of JavaScript*/


</head>
<body>

<div class="wideBox">
  <h1>Wave Web App</h1>
  <h2>Place the following waves in the correct order</h2>
</div>

<div id="content">

  <div id="cardPile"> </div>
  <div id="cardSlots"> </div>

  <div id="submitBox">
    <a class="button" data-reveal-id="Submit">Submit</a>
 
    <div id="Submit" class="reveal"  data-reveal aria-labelledby="module1Title" aria-hidden="true" role="dialog">
    <form action="https://ww2.shsu.edu/mail04wp/formmail.php" method="post" enctype="multipart/form-data" >
                  <input type="hidden" value="4546" name="title"/>
                  <input type="hidden" value="Fname, Lname" name="required">
                  <input type="hidden"  value="http://www.shsu.edu/academics/continuing-education/completion-ceremony/thank-you-submission.html" name="redirect" id="redirect"/>
          


                       <p class="fhalf"><strong>First Name<br></strong><input id="Fname" name="Fname" type="text" required/>
                      <p class="lhalf"><strong>Last Name<br></strong><input id="Lname" name="Lname" type="text" required/>
                      <p class="fhalf"><strong>Date<br></strong><input type="date" id="myDate"  />

                      <script type="text/javascript">
                      function SetDate(){
                        var date = new Date();

                        var day = date.getDate();
                        var month = date.getMonth() + 1;
                        var year = date.getFullYear();

                        if (month < 10) month = "0" + month;
                        if (day < 10) day = "0" + day;

                        var today = month + "/" + day + "/" + year;


                        document.getElementById('myDate').value = today;
                      }
                      </script>
                      <body onload="SetDate();">

                      <p class="fhalf"><strong>Your Answer</strong> <br> <input  id="answer" type="number" name="answer" value= #cardSlots disabled />
                        
                        <script type="text/javascript">
                        function fillAnswer(f) {
                            f.answer.value = f.cardNumber.value;
                          }
                        </script>
                        <body onload="fillAnswer();">

                        <br/>
                        <br/>
                      <input type="submit" value="Submit"/>

                    
              </form>
  <a class="close-reveal-modal" aria-label="Close">&#215;</a>
      </div>
 
    </div>

</div>



</body>
</html>

