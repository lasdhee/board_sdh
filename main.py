from board_dao import *

board_dao = BoardDAO()

while True:

    print("=" * 40)
    print("1.글 목록  2.글 등록  3.글 조회  4.글 삭제  5.글 수정  6.댓글 등록  7.댓글 삭제  0.종료")
    print("=" * 40)

    menu = input("선택 > ")

    if menu == "1":

        boards = board_dao.select_all()

        print()
        print("번호 제목 내용 작성자 작성일")
        print("-" * 40)

        for board in boards:

            print(
                board[0],
                board[1],
                board[2],
                board[3],
                board[4]
            )

    elif menu == "2":

        title = input("제목 : ")
        content = input("내용 : ")
        writer = input("작성자 : ")

        board_dao.insert_board(
            title,
            content,
            writer
        )

        print("등록 완료")

    elif menu == "3":

        num = input("번호 : ")

        board = board_dao.select_one(num)

        if board:

            print()
            print("번호 :", board[0])
            print("제목 :", board[1])
            print("내용 :", board[2])
            print("작성자 :", board[3])
            print("작성일 :", board[4])
            
            comments = board_dao.select_comments(num)
        
            print("\n[댓글 목록]")

            for comment in comments:
                print()
                print("댓글번호 :", comment[0])
                print("작성자 :", comment[3])
                print("내용 :", comment[2])

    elif menu == "4":

        num = input("삭제 번호 : ")

        board_dao.delete_board(num)

        print("삭제 완료")

    elif menu == "5":

        num = input("수정할 글 번호 : ")

        board = board_dao.select_one(num)

        if board:

            print("현재 제목 : ", board[1])
            print("현재 내용 : ", board[2])

            title = input("새 제목 : ")
            content = input("새 내용 : ")
            
            board_dao.update_board(
                num,
                title,
                content
            )

        print("수정 완료")

    elif menu == "6":

        board_id = input("게시글 번호 : ")
        
        board = board_dao.select_one(board_id)

        if board:

            content = input("댓글 내용 : ")
            writer = input("작성자 : ")

            board_dao.insert_comment(
                board_id,
                content,
                writer
            )

            print("댓글 등록 완료")

        else:
            print("존재하지 않는 게시글입니다.")

    elif menu == "7":

        board_id = input("게시글 번호 : ")

        comments = board_dao.select_comments(board_id)

        if comments:

            print("\n[댓글 목록]")

            for comment in comments:

                print()
                print("댓글번호 :", comment[0])
                print("작성자 :", comment[3])
                print("내용 :", comment[2])

            comment_id = input("\n삭제할 댓글 번호 : ")

            board_dao.delete_comment(comment_id)

            print("댓글 삭제 완료")

        else:

            print("댓글이 없습니다.")

    elif menu == "0":

        print("프로그램 종료")
        break
