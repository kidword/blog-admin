import request from '@/utils/request'

export function addArticle(data) {
  return request({
    url: '/add/blog/',
    method: 'post',
    data
  })
}
