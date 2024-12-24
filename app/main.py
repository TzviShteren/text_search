from app.repository.clearing_information import clearing_events, clearing_news
from app.repository.generic_actions import delete_all_events, insert_to_elasticsearch_events


def main():
    delete_all_events('events')
    delete_all_events('news')
    insert_to_elasticsearch_events(clearing_events(), 'events')
    insert_to_elasticsearch_events(clearing_news(), 'news')


if __name__ == '__main__':
    main()