import axios from 'axios'

var instance = axios.create({
    baseURL: 'http://localhost:5000',
    timeout: 20000
});

const requests = (before) => {
    return new Promise((resolve, reject) => {
        instance({
            url: before.url,
            method: before.method,
            data: before.params
        }).then(res => {
            // console.log(res);
            if (res.status === 200) {
                resolve(res.data);
            } else {
                throw res;
            }
        }).catch(err => {
            reject(err);
        })
    })
};

export default requests