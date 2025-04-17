// axios.get = token이 없음
// axiosInstance.get = token이 있음

let headers = {
    'X-CSRFToken' : getCookie('csrftoken')
}

const axiosInstance = axios.create({
    baseURL: '/',
    headers: headers
})