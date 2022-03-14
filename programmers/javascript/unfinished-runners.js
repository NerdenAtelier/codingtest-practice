/*
문제 정의: 
참가자 중 한 명만 완주하지 못했을 때, 미완주자의 이름을 return

제한사항: 
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

입출력 예시:
participant: ["leo", "kiki", "eden"]
completion: ["eden", "kiki"]
return: "leo"
*/

//브루트 포스를 이용하면 메모리 초과가 날 수 있음
//해시테이블을 이용하여 참가자+1, 완주자-1을 하여 값이 1인 사람 찾기
//JS에서는 객체나 Map을 이용할 수 있다

function solution(participant, completion) {
  runners = {};

  for (let person of participant) {
    runners[person] = runners[person] ? runners[person] + 1 : 1;
  }
  for (let person of completion) {
    runners[person] -= 1;
  }

  for (let key in runners) {
    if (runners[key] === 1) {
      return key;
    }
  }
}
