<template>
    <p>This is the Anagram Game Vue.</p>
    <div>
        <div>
            <label for="user-name">Username</label>
            <input type="text" name="user-name" id="user-name" v-model="userName"/>
        </div>
        <div>
            <label for="score">Score</label>
            <input type="number" name="score" id="score" v-model="score"/>
        </div>
        <button @click="recordScore">Record Score</button>
    </div>
</template>

<style>
div, label {
    padding: 0.2rem;
}
</style>

<script>
export default {
    name:'AnagramGame',
    data() {
        return {
            userName: '',
            score: 0
        }
    },
    methods: {
        async recordScore(){
            const data = {
                "user-name": this.userName,
                "score": this.score,
                "game": "ANAGRAM"
            };
            const response = (await this.axios.post("/record-score/", data)).data;
            console.log(response);
        }
    }
}
</script>

<!--
name: 'MathGame':
Bu, Vue bileşeninin adını belirtir.

data() { ... }:
Bu bölüm, bileşenin içindeki veri durumunu (state) tanımlar. 

methods: { ... }:
Bu bölüm, bileşen içinde kullanılabilir fonksiyonları (metodları) tanımlar. Bu örnekte, recordScore adında bir metod tanımlanmıştır. 

async recordScore() { ... }: Bu, bir asenkron fonksiyonun (async function) tanımını belirtir. 

const data = { ... }: Bir JSON nesnesi oluşturulur. Bu nesne, kullanıcının adını (userName), puanını (score) ve oyun türünü (game) içerir.

const response = ...: axios adlı bir HTTP istemcisi kullanılarak bir POST isteği gönderilir. Bu istek, "/record-score/" yoluna data nesnesini içeren JSON verisini içerir. Gelen veri isteği beklerken await anahtar kelimesi ile işlenir ve yanıtın verisine erişmek için .data özelliği kullanılır.

console.log(response);: İstek sonrası dönen yanıt (response) konsola yazdırılır. 
-->