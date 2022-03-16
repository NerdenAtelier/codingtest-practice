/*
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한사항:
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

입출력:
progresses : [93, 30, 55]
speeds : [1, 30, 5]
return : [2, 1]
*/

// 기능들은 우선순위에 따라 배치되어 있으므로, 순서를 그대로 지키면서 배포되어야 한다.
// 여기에서의 핵심은
// (1) 기능마다 남은 개발 기간이 며칠인가
// (2) 어떤 후속작업은 선행작업과 같이 배포되고, 어떤 건 아닌가
// 이는 각 기능마다 남은 개발 기간을 계산한 새로운 Queue를 만들고 순서대로 빼내면서,
// 그 뒤에 있는 기능의 개발 기간이 현재 개발 기간보다 짧다면 함께 배포한다는 논리로 설명이 가능하다.
// 결과적으로는 '기능별로 남은 개발 기간이 담겨 있는 Queue'를 만든다면 수월하게 해결할 수 있다.

function solution(progresses, speeds) {
  const answer = [];

  const leftDays = [];

  progresses.forEach((value, idx) => {
    let left = 100 - value;
    let speed = speeds[idx];

    if (left % speed === 0) {
      leftDays.push(left / speed);
    } else {
      leftDays.push(parseInt(left / speed) + 1);
    }
  });

  while (leftDays.length > 0) {
    let task = leftDays.shift();
    let count = 1;

    if (leftDays.length === 0) {
      answer.push(count);
      break;
    }

    while (leftDays.length > 0 && leftDays[0] <= task) {
      leftDays.shift();
      count += 1;
    }

    answer.push(count);
  }

  return answer;
}
