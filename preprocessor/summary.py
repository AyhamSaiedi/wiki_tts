from numpy import mod


def article_intro(text, title):
    """ Selects a few paragraphs from the article and starts with the paragraphs where the title is. """

    if title is None:
        return None
    
    if text is None:
        return None


    def select_paragraph(text_select, title_select, delimiter='\n'):
        
        l = [p for p in text_select.split(delimiter) if title_select in p]

        if l:
            return l
        else:
            ### ALTERNATIVE TO RETURNING NONE??? ###
            return None
   
    list_of_paragraphs = select_paragraph(text, title, delimiter='\n')

    if list_of_paragraphs is not None:
        to_string = ''.join(list_of_paragraphs)
        testing_input_text = text.split('\n')
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


    result = modifying_summary(to_string, testing_input_text)
    return result

