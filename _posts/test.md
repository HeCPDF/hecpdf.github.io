# 优化算法——牛顿法(Newton Method)

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[zhiyong_will](https://felix.blog.csdn.net "zhiyong_will")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png) 已于
2022-04-24 17:40:19 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量10w+ ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏 277

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png) 点赞数
49

分类专栏： [优化算法](https://blog.csdn.net/google19890102/category_9265873.html) 文章标签：
[优化算法](https://so.csdn.net/so/search/s.do?q=%E4%BC%98%E5%8C%96%E7%AE%97%E6%B3%95&t=all&o=vip&s=&l=&f=&viparticle=)
[牛顿法](https://so.csdn.net/so/search/s.do?q=%E7%89%9B%E9%A1%BF%E6%B3%95&t=all&o=vip&s=&l=&f=&viparticle=)
[机器学习](https://so.csdn.net/so/search/s.do?q=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&t=all&o=vip&s=&l=&f=&viparticle=)

于 2014-11-13 22:00:59 首次发布

版权声明：本文为博主原创文章，遵循[ CC 4.0 BY-SA ](http://creativecommons.org/licenses/by-
sa/4.0/)版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/google19890102/article/details/41087931>

版权

[ ![](https://img-
blog.csdn.net/20160516094032667?imageView2/1/w/224/h/224/interlace/1) 优化算法
专栏收录该内容 ](https://blog.csdn.net/google19890102/category_9265873.html "优化算法")

16 篇文章 297 订阅

订阅专栏

## 一、牛顿法概述

    除了前面说的梯度下降法，牛顿法也是机器学习中用的比较多的一种优化算法。牛顿法的基本思想是利用迭代点 ![](https://i-blog.csdnimg.cn/blog_migrate/7963f653c6bcc6087fd05595dbbfc8f5.gif)处的一阶导数(梯度)和二阶导数(Hessen矩阵)对目标函数进行二次函数近似，然后把二次模型的极小点作为新的迭代点，并不断重复这一过程，直至求得满足精度的近似极小值。牛顿法的速度相当快，而且能高度逼近最优值。牛顿法分为基本的牛顿法和全局牛顿法。 

## 二、基本牛顿法

### 1、基本牛顿法的原理

    基本牛顿法是一种是用导数的算法，它每一步的迭代方向都是沿着当前点函数值下降的方向。 

    我们主要集中讨论在一维的情形，对于一个需要求解的优化函数 ![](https://i-blog.csdnimg.cn/blog_migrate/e964fbc49bf64153249bb5ebf910d313.gif)，求函数的极值的问题可以转化为求导函数 ![](https://i-blog.csdnimg.cn/blog_migrate/95229037a6fd591c2052a1c1fbc8a357.gif)。对函数 ![](https://i-blog.csdnimg.cn/blog_migrate/e964fbc49bf64153249bb5ebf910d313.gif)进行泰勒展开到二阶，得到 

![](https://i-blog.csdnimg.cn/blog_migrate/e964fbc49bf64153249bb5ebf910d313.gif=f%5Cleft&space;%28&space;x_k&space;%5Cright&space;%29+%7Bf%7D'%5Cleft&space;%28&space;x_k&space;%5Cright&space;%29%5Cleft&space;%28&space;x-x_k&space;%5Cright&space;%29+%5Cfrac%7B1%7D%7B2%7D%7Bf%7D''%5Cleft&space;%28&space;x_k&space;%5Cright&space;%29%5Cleft&space;%28&space;x-x_k&space;%5Cright&space;%29%5E2)

对上式求导并令其为0，则为

![](https://i-blog.csdnimg.cn/blog_migrate/cea9215fa36e075a05c7d12ca3717e7d.gif)

即得到

![](https://i-blog.csdnimg.cn/blog_migrate/6373737ead4bb0cf7833cdfbb1a146ed.gif)

这就是牛顿法的更新公式。

### 2、基本牛顿法的流程

  1. 给定终止误差值![](https://i-blog.csdnimg.cn/blog_migrate/4689b74badbfa7bffb6a1211d0b10880.gif)，初始点![](https://i-blog.csdnimg.cn/blog_migrate/4daf6daebd2e312f2363362749065163.gif)，令![](https://i-blog.csdnimg.cn/blog_migrate/d7ed1193999d5fedd6a7f0af2116a485.gif)；
  2. 计算![](https://i-blog.csdnimg.cn/blog_migrate/0e9aabbf2e63d7f7cacd2bc92d9e5c87.gif)，若![](https://i-blog.csdnimg.cn/blog_migrate/95b4b92cff764a42ed3acad5f40d3672.gif)，则停止，输出![](https://i-blog.csdnimg.cn/blog_migrate/83ac27f02ee581291c5dd27c695f8485.gif)；
  3. 计算![](https://i-blog.csdnimg.cn/blog_migrate/a92cec8517f132d083a991e66eaeacf9.gif)，并求解线性方程组得解![](https://i-blog.csdnimg.cn/blog_migrate/0215dc9c31f838be1e7a65e107582eb7.gif)：![](https://i-blog.csdnimg.cn/blog_migrate/11fc73ac8d8fa5cf945915d8f266c129.gif)；
  4. 令![](https://i-blog.csdnimg.cn/blog_migrate/46d24007bc531d12d12aeaee9d1069f6.gif)，![](https://i-blog.csdnimg.cn/blog_migrate/6453a0cab6041218415e36577278c03d.gif)，并转2。

## 三、全局牛顿法

    牛顿法最突出的优点是收敛速度快，具有局部二阶收敛性，但是，基本牛顿法初始点需要足够“靠近”极小点，否则，有可能导致算法不收敛。这样就引入了全局牛顿法。 

### 1、全局牛顿法的流程

  1. 给定终止误差值![](https://i-blog.csdnimg.cn/blog_migrate/4689b74badbfa7bffb6a1211d0b10880.gif)，![](https://i-blog.csdnimg.cn/blog_migrate/19bdf3816d8eba24243c7eb0e939a286.gif)，![](https://i-blog.csdnimg.cn/blog_migrate/5f44c66b270957aba967e30aaf7b359a.gif)，初始点![](https://i-blog.csdnimg.cn/blog_migrate/4daf6daebd2e312f2363362749065163.gif)，令![](https://i-blog.csdnimg.cn/blog_migrate/d7ed1193999d5fedd6a7f0af2116a485.gif)；
  2. 计算![](https://i-blog.csdnimg.cn/blog_migrate/0e9aabbf2e63d7f7cacd2bc92d9e5c87.gif)，若![](https://i-blog.csdnimg.cn/blog_migrate/95b4b92cff764a42ed3acad5f40d3672.gif)，则停止，输出![](https://i-blog.csdnimg.cn/blog_migrate/83ac27f02ee581291c5dd27c695f8485.gif)；
  3. 计算![](https://i-blog.csdnimg.cn/blog_migrate/a92cec8517f132d083a991e66eaeacf9.gif)，并求解线性方程组得解![](https://i-blog.csdnimg.cn/blog_migrate/0215dc9c31f838be1e7a65e107582eb7.gif)：![](https://i-blog.csdnimg.cn/blog_migrate/11fc73ac8d8fa5cf945915d8f266c129.gif)；
  4. 记![](https://i-blog.csdnimg.cn/blog_migrate/5caf77982da85def98c7abfee05a43b2.gif)是不满足下列不等式的最小非负整数![](https://i-blog.csdnimg.cn/blog_migrate/20ddd8181c2e0d0fb893637e8572d475.gif)：![](https://i-blog.csdnimg.cn/blog_migrate/3e4c0d84c38490baf9e2b6c747ea789c.gif)；
  5. 令![](https://i-blog.csdnimg.cn/blog_migrate/ef8d7fa74e578956472cc01cfbe67713.gif)，![](https://i-blog.csdnimg.cn/blog_migrate/892931af10729cfcf42cc006b3488663.gif)，![](https://i-blog.csdnimg.cn/blog_migrate/6453a0cab6041218415e36577278c03d.gif)，并转2。

### 2、Armijo搜索

    全局牛顿法是基于Armijo的搜索，满足Armijo准则： 

给定
![](https://i-blog.csdnimg.cn/blog_migrate/e2ed58b05b8134252a591bcf93709d4c.gif)，
![](https://i-blog.csdnimg.cn/blog_migrate/5f44c66b270957aba967e30aaf7b359a.gif)，令步长因子
![](https://i-blog.csdnimg.cn/blog_migrate/8509769a3fea78a8c1b0158e8d9e66fc.gif)，其中
![](https://i-blog.csdnimg.cn/blog_migrate/5caf77982da85def98c7abfee05a43b2.gif)是满足下列不等式的最小非负整数:

![](https://i-blog.csdnimg.cn/blog_migrate/8962088ed0464e018ff269798c9e3353.gif)

## 四、算法实现

    实验部分使用Java实现，需要优化的函数 ![](https://i-blog.csdnimg.cn/blog_migrate/e964fbc49bf64153249bb5ebf910d313.gif=x%5E2-3x+1)，最小值为 ![](https://i-blog.csdnimg.cn/blog_migrate/e6b7a24307781d32a4549164ae5f915f.gif)。 

### 1、基本牛顿法Java实现

    
    
    package org.algorithm.newtonmethod;
    
    /**
     * Newton法
     * 
     * @author dell
     * 
     */
    public class NewtonMethod {
    	private double originalX;// 初始点
    	private double e;// 误差阈值
    	private double maxCycle;// 最大循环次数
    
    	/**
    	 * 构造方法
    	 * 
    	 * @param originalX初始值
    	 * @param e误差阈值
    	 * @param maxCycle最大循环次数
    	 */
    	public NewtonMethod(double originalX, double e, double maxCycle) {
    		this.setOriginalX(originalX);
    		this.setE(e);
    		this.setMaxCycle(maxCycle);
    	}
    
    	// 一系列get和set方法
    	public double getOriginalX() {
    		return originalX;
    	}
    
    	public void setOriginalX(double originalX) {
    		this.originalX = originalX;
    	}
    
    	public double getE() {
    		return e;
    	}
    
    	public void setE(double e) {
    		this.e = e;
    	}
    
    	public double getMaxCycle() {
    		return maxCycle;
    	}
    
    	public void setMaxCycle(double maxCycle) {
    		this.maxCycle = maxCycle;
    	}
    
    	/**
    	 * 原始函数
    	 * 
    	 * @param x变量
    	 * @return 原始函数的值
    	 */
    	public double getOriginal(double x) {
    		return x * x - 3 * x + 2;
    	}
    
    	/**
    	 * 一次导函数
    	 * 
    	 * @param x变量
    	 * @return 一次导函数的值
    	 */
    	public double getOneDerivative(double x) {
    		return 2 * x - 3;
    	}
    
    	/**
    	 * 二次导函数
    	 * 
    	 * @param x变量
    	 * @return 二次导函数的值
    	 */
    	public double getTwoDerivative(double x) {
    		return 2;
    	}
    
    	/**
    	 * 利用牛顿法求解
    	 * 
    	 * @return
    	 */
    	public double getNewtonMin() {
    		double x = this.getOriginalX();
    		double y = 0;
    		double k = 1;
    		// 更新公式
    		while (k <= this.getMaxCycle()) {
    			y = this.getOriginal(x);
    			double one = this.getOneDerivative(x);
    			if (Math.abs(one) <= e) {
    				break;
    			}
    			double two = this.getTwoDerivative(x);
    			x = x - one / two;
    			k++;
    		}
    		return y;
    	}
    
    }
    



### 2、全局牛顿法Java实现

    
    
    package org.algorithm.newtonmethod;
    
    /**
     * 全局牛顿法
     * 
     * @author dell
     * 
     */
    public class GlobalNewtonMethod {
    	private double originalX;
    	private double delta;
    	private double sigma;
    	private double e;
    	private double maxCycle;
    
    	public GlobalNewtonMethod(double originalX, double delta, double sigma,
    			double e, double maxCycle) {
    		this.setOriginalX(originalX);
    		this.setDelta(delta);
    		this.setSigma(sigma);
    		this.setE(e);
    		this.setMaxCycle(maxCycle);
    	}
    
    	public double getOriginalX() {
    		return originalX;
    	}
    
    	public void setOriginalX(double originalX) {
    		this.originalX = originalX;
    	}
    
    	public double getDelta() {
    		return delta;
    	}
    
    	public void setDelta(double delta) {
    		this.delta = delta;
    	}
    
    	public double getSigma() {
    		return sigma;
    	}
    
    	public void setSigma(double sigma) {
    		this.sigma = sigma;
    	}
    
    	public double getE() {
    		return e;
    	}
    
    	public void setE(double e) {
    		this.e = e;
    	}
    
    	public double getMaxCycle() {
    		return maxCycle;
    	}
    
    	public void setMaxCycle(double maxCycle) {
    		this.maxCycle = maxCycle;
    	}
    
    	/**
    	 * 原始函数
    	 * 
    	 * @param x变量
    	 * @return 原始函数的值
    	 */
    	public double getOriginal(double x) {
    		return x * x - 3 * x + 2;
    	}
    
    	/**
    	 * 一次导函数
    	 * 
    	 * @param x变量
    	 * @return 一次导函数的值
    	 */
    	public double getOneDerivative(double x) {
    		return 2 * x - 3;
    	}
    
    	/**
    	 * 二次导函数
    	 * 
    	 * @param x变量
    	 * @return 二次导函数的值
    	 */
    	public double getTwoDerivative(double x) {
    		return 2;
    	}
    
    	/**
    	 * 利用牛顿法求解
    	 * 
    	 * @return
    	 */
    	public double getGlobalNewtonMin() {
    		double x = this.getOriginalX();
    		double y = 0;
    		double k = 1;
    		// 更新公式
    		while (k <= this.getMaxCycle()) {
    			y = this.getOriginal(x);
    			double one = this.getOneDerivative(x);
    			if (Math.abs(one) <= e) {
    				break;
    			}
    			double two = this.getTwoDerivative(x);
    			double dk = -one / two;// 搜索的方向
    			double m = 0;
    			double mk = 0;
    			while (m < 20) {
    				double left = this.getOriginal(x + Math.pow(this.getDelta(), m)
    						* dk);
    				double right = this.getOriginal(x) + this.getSigma()
    						* Math.pow(this.getDelta(), m)
    						* this.getOneDerivative(x) * dk;
    				if (left <= right) {
    					mk = m;
    					break;
    				}
    				m++;
    			}
    			x = x + Math.pow(this.getDelta(), mk)*dk;
    			k++;
    		}
    		return y;
    	}
    }
    



### 3、主函数

    
    
    package org.algorithm.newtonmethod;
    
    /**
     * 测试函数
     * @author dell
     *
     */
    public class TestNewton {
    	public static void main(String args[]) {
    		NewtonMethod newton = new NewtonMethod(0, 0.00001, 100);
    		System.out.println("基本牛顿法求解：" + newton.getNewtonMin());
    
    		GlobalNewtonMethod gNewton = new GlobalNewtonMethod(0, 0.55, 0.4,
    				0.00001, 100);
    		System.out.println("全局牛顿法求解：" + gNewton.getGlobalNewtonMin());
    	}
    }
    

  


