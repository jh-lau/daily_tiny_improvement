"""
  @Author       : liujianhan
  @Date         : 2019/12/31 下午4:33
  @Project      : DailyTinyImprovement
  @FileName     : distance_with_nature.py
  @Description  : Placeholder
"""
import distance
origin_title = ''
segment_result = ''

for i, cut_word in enumerate(segment_result):
    if distance.levenshtein(cut_word.word, origin_title) == 1 and len(cut_word.word) == len(origin_title):
        content_string = content_string.replace(cut_word.word, origin_title)
    if distance.levenshtein(cut_word.word, origin_title) == 1 and str(cut_word.nature) in ['nr', 'nrf']:
        if str(segment_result[i+1].nature) in ['nr', 'nrf', 'b', 'x']:
            translated_word = cut_word.word + segment_result[i+1].word
        else:
            translated_word = cut_word.word
        print('translated word:',translated_word)
        content_string = content_string.replace(translated_word, origin_title)