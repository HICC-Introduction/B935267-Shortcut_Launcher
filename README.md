# B935267-Shortcut_Launcher


# 과제 내용

## 1단계

* 요약
    * 단축키 프로그램
        지정된 명령어를 클릭 한 번으로 바로 실행할 수 있는 프로그램을 개발한다.
* 기능
     * 2행 4열
     * 단일 윈도우
     * 버튼 클릭하면 지정된 명령어 실행
* 제약
     * 프로그램 크기 변화 없음
     * 명령어 고정
       * 버튼 1 : 메모장 실행 (명령: "notepad")
       * 버튼 2 : 계산기 실행 (명령: "calc")
       * 버튼 3 : 폴더 C:\ 열기 (명령: "c:\")
       * 버튼 4 : [google.com](http://google.com) 열기 (명령: "http://google.com")
 * 기타 버튼의 역할은 임의로 지정 혹은 지정하지 않기
 * 기본적으로 UI는 버튼만 한정
 * 윈도우 운영체제 작동(리눅스 유닉스 등은 고려하지 않음)
 * 윈도우의 크기는 가로 800, 세로 200으로 고정한다.


# 개발 사양
## 하드웨어
* CPU : Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz (8코어 Intel Core i9)
* RAM : 16.0GB
* SSD: 499.96GB
* GPU : Intel UHD Graphics 630 1536 MB

## 소프트웨어
* OS : Mac OS Catalina
* 개발 스택 : TKinter 
   * (선정 이유: 아직 python 자체에 익숙하지 않아 개발 스택으로는 더 단순하고 직관적인 TKinter선정)
* 개발 프로그램 : REPL
* 개발 언어 : Python v3.8.2

## 코드룰
   예시
    #변수명
    test_variable = 1

    #클래스명
    class test_class:
        def __init__(self):
            #프로퍼티명
            self.test_property = 1

        #메소드명
        def test_method(self):
            print(self.test_property)

    if __name__ == "__main__":
        test_variable = test_class(2)
        test_variable.test_method()
