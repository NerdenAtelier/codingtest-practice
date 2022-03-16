'''
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항:
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

입출력예:
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
return = [4, 1, 3, 0]
'''

# 노래의 고유 번호 = 배열에서의 인덱스 번호이다.
# 속한 노래의 재생 수 총 합이 가장 많은 장르부터
# -> 장르 내에서는 재생 수가 많은 곡부터
# -> 재생 수가 같다면 고유 번호가 낮은(빠른) 곡부터 이므로
# 최종적으로 데이터를 선별할 때에는 장르/재생 수/고유 번호가 모두 조회 가능해야 한다는 것이다.

# 두 개의 해시테이블 구조를 만들어서 이용한다.
# 장르별로 재생 수 총 합을 세기 위한 딕셔너리
# 장르별로 해당되는 노래들을 (곡 재생 수, 곡 고유 번호) 형태로 리스트에 담아 놓은 딕셔너리
# 1번 딕셔너리로부터, 재생 수 총 합에 따른 각 장르들 간의 순서를 얻을 수 있다.
# 이를 기반으로 2번 딕셔너리에 각 장르들에 접근하고,
# 2번 딕셔너리의 장르(Key)가 가진 값(List)을 각 재생 수별로 정렬하여
# 상위 2개의 고유번호를 최종 결과 리스트에 삽입한다.

import collections

def solution(genres, plays) :
    answer = []

    count_dict = collections.defaultdict(int)
    song_dict = collections.defaultdict(list)

    #주어진 2개의 배열을 기반으로 딕셔너리에 값을 삽입
    #인덱스 i 가 곡들의 고유 번호가 된다

    for i in range(len(genres)) :
        genre = genres[i]
        count = plays[i]
        count_dict[genre] += count
        song_dict[genre] += [(count, i)]

    #count_dict라는 딕셔너리로부터, genre_sorted라는 리스트를 만들어냄
    #해당 리스트 내에는 (장르, 총 재생 횟수)들이 총 재생 횟수의 내림차순으로 정렬
    #key=lambda x: x[1] 을 통해 count_dict의 value들을 기준으로 정렬
    #reverse=True 이므로 내림차순 정렬

    genre_sorted = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    #g, c는 장르, 총 재생 횟수
    for g, c in genre_sorted :
        #song_dict를 통해 장르별로 속한 곡에 접근
        #key=lambda x: (-x[0], x[1])
        #(1) 곡별 재생 횟수 내림차순 정렬 (2) 그게 같을 경우 고유 번호 오름차순 정렬
        song_dict[g] = sorted(song_dict[g], key=lambda x: (-x[0], x[1]))
        #상위 2개만 최종 결과에 반영
        answer += [i for (c, i) in song_dict[g][:2]]

    return answer