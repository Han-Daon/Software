Auto_Easteregg 파일은 계산기에 이스터 에그를 입력하자 마자 
자동으로 인식하여 특정 출력문을 만들어주는 기능을 구현해 봤습니다.
입력시 자동 출력 기능 자체는 구현이 되었으나, 계산기 기능과 합치지 못하였습니다.

cmd에 pip install keyboard 를 입력하여 keyboard 라이브러리를 설치 해야합니다

-계산기와 결합의 문제점
하드웨어적 키입력 인식방식으로 처음에 피연산자를 입력 받을 때부터 해당 함수는 시행이 되어 있어야 이스터 에그값이 입력시 자동으로 인식을 합니다. 하지만 이렇게 된다면 
피연산자에 입력과 이스터에그 인식이 동시에 일어나 제대로된 계산 기능이 제한됩니다.
