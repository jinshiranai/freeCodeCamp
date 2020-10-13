// Card counting function exercise

var count = 0;

function cc(card) {
  // Only change code below this line
  if (card >=2 && card <= 6) {
    count++;
  } else if (card >= 7 && card <= 9) {
    count += 0;
  } else if (card == 10) {
    count--;
  } else if (card == 'J') {
    count--;
  } else if (card == 'Q') {
    count--;
  } else if (card == 'K') {
    count--;
  } else if (card == 'A') {
    count--;
  }

  if (count > 0) {
    var countString = count.toString();
    return countString += ' Bet';
  } else if (count <= 0) {
    var countString = count.toString();
    return countString += ' Hold';
  }

    // Only change code above this line
}

cc(2); cc(3); cc(7); cc('K'); cc('A');
