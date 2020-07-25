import requests from '@/utils/requests'


export function getDBList() {
    return requests({
        url: '/db',
        method: 'GET',
        params: '0'
    })
}