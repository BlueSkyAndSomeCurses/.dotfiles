"""
module with functions to analyse browser history
"""

def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)

    >>> get_url_info([('https://www.google.com/=UTF-8', 'youtube\
'youtube - Пошук Google', '2023-10-21', '14:26:54.304747', 1117989),\
('https://www.math-anal.ys.com/?hl=uk&gl=UA', 'restricted-content',\
'2023-01-21', '14:26:55.421209', 1757275),\
('https://www.math-anal.ys.com/?hl=uk&gl=UA', 'resticted-content',\
'2023-11-21', '14:26:55.421209', 757275)], 'https://www.math-anal.ys.com/?hl=uk&gl=UA')

    """

    output = []

    for visit in visits:
        if visit[0] == url:
            output.append(visit[1])
            output.append(visit[2])
            output.append(visit[3])
            output.append(0)
            output.append(0)
            break

    for visit in visits:
        if visit[0] == url:
            output[3] += 1
            output[4] += visit[4]

    output[4] //= output[3]

    return tuple(output)


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
