from numpy import mod


def article_intro(text, title):

    if title is None:
        return None
    
    if text is None:
        return None

    def select_paragraph(text_select, title_select, delimiter='\n'):
        
        l = [p for p in text_select.split(delimiter) if title_select in p]

        if l:
            return l
        else:
            return None
   
    paragraph_begin = select_paragraph(text, title, delimiter='\n')

    if paragraph_begin is not None:
        std = ''.join(paragraph_begin)
        list = text.split('\n')
    else:
        return None

    def modifying_summary(paragraph, test_list):
        
        if (paragraph is None):
            return None

        elif any(paragraph in i for i in test_list):
            index_int = test_list.index(paragraph)
            matching = test_list[index_int:]
            essential = matching[:5]
            summary_stringified = ''.join([str(it) for it in essential])
            
            return summary_stringified.strip()


    result = modifying_summary(std, list)
    return result
