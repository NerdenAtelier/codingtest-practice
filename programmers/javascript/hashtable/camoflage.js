/*
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항:
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.

입출력예시:
clothes: [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
return : 5
*/

// 스파이가 매번 다른 옷차림을 하도록, 가진 옷들을 이용해 만들 수 있는 조합의 수를 찾는 문제이다.
// 옷 카테고리의 종류는 딱히 지정되어 있지 않고, 의상의 수는 1~30개이다.
// 해시 구조를 이용하여 카테고리별로 소지한 옷을 분류하여 조합을 만들어야 한다.

// 스파이는 하루에 최소 한 개의 의상을 입음 -> 안 사용하는 카테고리가 있을 수 있다.
// 따라서 가능한 조합의 수는 카테고리마다 [각 카테고리별 의상 수 + 1] 를 구한 후,
// 그 수를 모두 곱한 후 마지막에 1을 빼주면 (아무 것도 안 입은 경우) 가능한 조합의 수가 나올 것이다.

function solution(clothes) {
  let answer = 1;
  closet = {};

  for (let cloth of clothes) {
    closet[cloth[1]]
      ? closet[cloth[1]].push(cloth[0])
      : (closet[cloth[1]] = [cloth[0]]);
  }
  for (key in closet) {
    answer *= closet[key].length + 1;
  }

  return answer - 1;
}
