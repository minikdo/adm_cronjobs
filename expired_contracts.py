from notification_manager import NotificationManager


def main():
    nm = NotificationManager()

    ids = nm.get_ids("""select id from est where wyl < now() and status=0""")
    template = 'expired'
    subject = 'umowy zakończone'
    
    nm.notify(template, subject, ids)
    

if __name__ == '__main__':
    main()



