module.exports = {
    publicPath: 'http://localhost:8080', // The base URL where your app will be deployed.
    outputDir: '../static/dist', // The path for where files will be output when the app is built. ../ means one step up folder.
    indexPath: '../../templates/_base_vue.html', // The path for generated index file
    
    configureWebpack: {
        devServer: {
            devMiddleware: {
                writeToDisk: true
            }
        }
    }
};



// publicPath: Bu seçenek, uygulamanızın kök URL'sini belirtir. Bu, uygulamanızın dağıtılacağı sunucu veya konumun temel adresidir. 

// outputDir: Derlendiğinde üretilen dosyaların nereye yerleştirileceğini belirtir. Bu yol, uygulamanızın derlenmiş üretim sürümünün çıktısının konulacağı konumu belirtir.

// indexPath: Oluşturulan index dosyasının yolu. Bu genellikle projenizin ana şablon dosyasına yol belirten bir değerdir. Örneğin, Django gibi bir şablon motoru kullanıyorsanız, burada ana şablonunuzu belirtirsiniz.

// configureWebpack: Bu bölüm, Webpack yapılandırması hakkında özelleştirmeler yapmanızı sağlar. Bu örnekte devServer altında yapılandırmalar yapılıyor.

// devServer.devMiddleware.writeToDisk: Bu değer true olarak ayarlandığında, geliştirme sunucusu, üretilen dosyaları diskte fiziksel olarak depolar. Bu genellikle geliştirme sırasında faydalıdır, çünkü oluşturulan dosyaları inceleyebilirsiniz.