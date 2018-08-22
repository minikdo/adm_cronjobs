from backend_service import BackendService

def main():
    # update photo count in est main table
    bs = BackendService()

    print(bs.photo_count())


if __name__ == '__main__':
    main()
            
