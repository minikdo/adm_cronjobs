from notification_manager import NotificationManager
from backend_service import BackendService

def main():
    nm = NotificationManager('expired')

    bs = BackendService()
    
    # ids = bs.expired_ids(7)
    ids = bs.no_photo_ids()

    email_to = bs.get_active_users()
    
    subject = 'umowy zakończone'

    body = nm.generate_body('expired', ids, context={'pow_label': 'pow.',
                                                     'name_label': 'nazwa'})
    
    nm.notify(subject, body, email_to)
    

if __name__ == '__main__':
    main()



