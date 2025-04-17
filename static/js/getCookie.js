// 쿠키 이름(name)을 입력받아 해당 쿠키 값을 반환하는 함수
function getCookie(name) {
    // 반환할 쿠키 값을 저장할 변수
    let cookieValue = null;
    
    // document.cookie가 비어 있지 않은 경우
    if (document.cookie && document.cookie !== '') {
        // 쿠키 문자열을 '; '로 분리해 배열로 변환
        const cookies = document.cookie.split(';');
        
        // 각 쿠키를 순회하며 이름이 일치하는 쿠키 찾기
        for (let i = 0; i < cookies.length; i++) {
            // 쿠키 문자열에서 앞뒤 공백 제거
            const cookie = cookies[i].trim();
            
            // 쿠키 이름이 입력된 name과 일치하는지 확인
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                // '=' 뒤의 값을 추출해 cookieValue에 저장
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    
    // 찾은 쿠키 값 반환 (없으면 null 반환)
    return cookieValue;
}