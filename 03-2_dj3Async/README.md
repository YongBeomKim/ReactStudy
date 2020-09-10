## Async & Await

### Promise of Axios

```javascript
const on_click = async () => {
	try {
		const response = await axios.get(
			'https://jsonplaceholder.typicode.com/todos/1',
		);
		setData(response.data);
	} catch (error) {
		console.log(error);
	}
};
```

try/catch 문 안에서 `await` 을 사용하여 요청을보내면 응답받은 값을 같은 스코프 내에서 처리가 가능해져서 훨씬 보기도 편하고, **코드도 간결** 해지고 **콜백 지옥 현상도 발생하지 않는다.**

다만 한가지 문제라면 `async/await` 에서는 요청을 한번에 모아서 보내는 방식이라 catch부분의 에러의 구분이 되지않는다. 즉, try 안에서 3개의 요청을 보냈지만 **이중 어떤것이라도 실패한다면 catch로 빠지기 때문에** 요청에 실패한다면 디버깅이 어렵다는 단점이 있다. [출처:Ryu.log](https://ryulog.tistory.com/139)
