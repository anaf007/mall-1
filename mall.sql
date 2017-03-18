/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50537
Source Host           : localhost:3306
Source Database       : mall

Target Server Type    : MYSQL
Target Server Version : 50537
File Encoding         : 65001

Date: 2017-03-06 22:33:23
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `address`
-- ----------------------------
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_address_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of address
-- ----------------------------
INSERT INTO address VALUES ('1', '3', '安海明', '望洲路', '18977771077', '1');
INSERT INTO address VALUES ('2', '1', '发货人', '北京路', '18977777777', '1');

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO admin VALUES ('2', '1', '0');

-- ----------------------------
-- Table structure for `alembic_version`
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO alembic_version VALUES ('bb8148e0f96e');

-- ----------------------------
-- Table structure for `banners`
-- ----------------------------
DROP TABLE IF EXISTS `banners`;
CREATE TABLE `banners` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link` varchar(255) DEFAULT NULL,
  `photo_url` varchar(255) DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of banners
-- ----------------------------

-- ----------------------------
-- Table structure for `base_products`
-- ----------------------------
DROP TABLE IF EXISTS `base_products`;
CREATE TABLE `base_products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `Original_price` decimal(15,2) DEFAULT NULL,
  `Special_price` decimal(15,2) DEFAULT NULL,
  `note` varchar(1000) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of base_products
-- ----------------------------

-- ----------------------------
-- Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `pid` int(11) DEFAULT '0',
  `seller_id` int(11) DEFAULT NULL,
  `ico` varchar(255) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO category VALUES ('2', '蔬菜豆蘑菇', '0', null, '', '100', '0');
INSERT INTO category VALUES ('3', '新鲜蔬菜', '2', null, '', '100', '0');
INSERT INTO category VALUES ('4', '新鲜蘑菇', '2', null, '', '100', '0');
INSERT INTO category VALUES ('5', '新鲜豆类', '2', null, '', '100', '0');

-- ----------------------------
-- Table structure for `delivery`
-- ----------------------------
DROP TABLE IF EXISTS `delivery`;
CREATE TABLE `delivery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `score_count` int(11) DEFAULT NULL,
  `integral` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of delivery
-- ----------------------------

-- ----------------------------
-- Table structure for `ean`
-- ----------------------------
DROP TABLE IF EXISTS `ean`;
CREATE TABLE `ean` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `products` int(11) DEFAULT NULL,
  `ean` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ean
-- ----------------------------

-- ----------------------------
-- Table structure for `goods`
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `id_md5` varchar(16) DEFAULT NULL,
  `original_price` decimal(10,2) DEFAULT NULL,
  `special_price` decimal(10,2) DEFAULT NULL,
  `vip_price` decimal(10,2) DEFAULT NULL,
  `note` varchar(1000) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `combination` varchar(255) DEFAULT NULL,
  `scores` int(11) DEFAULT NULL,
  `goodpost` int(11) DEFAULT NULL,
  `badpost` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `thumbnail` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `attribute` int(11) DEFAULT NULL,
  `excellent` int(11) DEFAULT NULL,
  `new_goods` int(11) DEFAULT NULL,
  `hot_goods` int(11) DEFAULT NULL,
  `limit_start_time_price` datetime DEFAULT NULL,
  `limit_end_time_price` datetime DEFAULT NULL,
  `promote_price` decimal(10,2) DEFAULT NULL,
  `integral` int(11) DEFAULT NULL,
  `view_count` int(11) DEFAULT NULL,
  `buy_count` int(11) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `goods_id` varchar(255) DEFAULT NULL,
  `goods_name` varchar(255) DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_goods_id_md5` (`id_md5`),
  KEY `ix_goods_seller_id` (`seller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO goods VALUES ('1', '1', '特价', 'a0b923820dcc509a', '2.99', '2.09', null, '烦烦烦', '3', '99', '', '0', '0', '0', '2017-02-27 09:03:52', '1', null, null, '1', '0', '1', '0', null, null, null, '1', '0', '0', '100', null, null, null);
INSERT INTO goods VALUES ('2', '1', 'ddd', '9d4c2f636f067f89', '9.99', '8.88', null, '', '3', '444', '', '0', '0', '0', '2017-02-27 09:06:26', '1', null, null, '1', '0', '1', '0', null, null, '6.66', '1', '0', '0', '100', null, null, null);
INSERT INTO goods VALUES ('3', '1', '555f', '4b5ce2fe28308fd9', '9.99', '8.88', null, '', '3', '333', '', '0', '0', '0', '2017-02-27 09:06:26', '1', null, null, '1', '0', '1', '0', null, null, '6.66', '1', '0', '0', '100', null, null, null);

-- ----------------------------
-- Table structure for `goods_thumbnail`
-- ----------------------------
DROP TABLE IF EXISTS `goods_thumbnail`;
CREATE TABLE `goods_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_id` int(11) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `thumbnail_status` int(11) DEFAULT NULL,
  `goods_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_thumbnail
-- ----------------------------

-- ----------------------------
-- Table structure for `orders`
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_name` varchar(100) DEFAULT NULL,
  `start_phone` varchar(20) DEFAULT NULL,
  `start_address` varchar(255) DEFAULT NULL,
  `end_name` varchar(100) DEFAULT NULL,
  `end_phone` varchar(20) DEFAULT NULL,
  `end_address` varchar(255) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL,
  `number` varchar(100) DEFAULT NULL,
  `number_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `express_type` varchar(100) DEFAULT NULL,
  `express_number` varchar(100) DEFAULT NULL,
  `freight` decimal(15,2) DEFAULT NULL,
  `discount` decimal(15,2) DEFAULT NULL,
  `pay` decimal(15,2) DEFAULT NULL,
  `pay_time` datetime DEFAULT NULL,
  `integral` int(11) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `evaluate_buyers` int(11) DEFAULT NULL,
  `evaluate_buyers_time` datetime DEFAULT NULL,
  `evaluate_buyers_note` varchar(1000) DEFAULT NULL,
  `evaluate_seller` int(11) DEFAULT NULL,
  `evaluate_seller_time` datetime DEFAULT NULL,
  `evaluate_seller_note` varchar(1000) DEFAULT NULL,
  `evaluate_transport` int(11) DEFAULT NULL,
  `evaluate_transport_time` datetime DEFAULT NULL,
  `evaluate_transport_note` varchar(1000) DEFAULT NULL,
  `reply` varchar(1000) DEFAULT NULL,
  `reply_time` datetime DEFAULT NULL,
  `transport_name` varchar(100) DEFAULT NULL,
  `transport_phone` varchar(15) DEFAULT NULL,
  `order_state` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO orders VALUES ('40', '发货人', '18977777777', '北京路', '安海明', '18977771077', '望洲路', '1', '19555625227SEQH95F', '2017-03-02 16:52:28', null, null, null, '3.00', null, '20.76', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0', '3');

-- ----------------------------
-- Table structure for `order_goods`
-- ----------------------------
DROP TABLE IF EXISTS `order_goods`;
CREATE TABLE `order_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` varchar(32) DEFAULT NULL,
  `goods_id` int(11) DEFAULT NULL,
  `count` float(11,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_goods
-- ----------------------------
INSERT INTO order_goods VALUES ('59', '19555619442LXU9QSF', '2', '1');
INSERT INTO order_goods VALUES ('60', '19555619442LXU9QSF', '3', '3');
INSERT INTO order_goods VALUES ('61', '19555625227SEQH95F', '2', '2');

-- ----------------------------
-- Table structure for `roles`
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `permissions` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_roles_default` (`default`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of roles
-- ----------------------------

-- ----------------------------
-- Table structure for `sellers`
-- ----------------------------
DROP TABLE IF EXISTS `sellers`;
CREATE TABLE `sellers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `number_md5` varchar(32) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `master` varchar(100) DEFAULT NULL,
  `self_business` int(11) DEFAULT NULL,
  `evaluate` int(11) DEFAULT NULL,
  `evaluate_count` int(11) DEFAULT NULL,
  `address_map` varchar(100) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_sellers_number_md5` (`number_md5`),
  UNIQUE KEY `ix_sellers_name` (`name`),
  UNIQUE KEY `ix_sellers_number` (`number`),
  UNIQUE KEY `ix_sellers_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sellers
-- ----------------------------
INSERT INTO sellers VALUES ('1', '1', '默认名称', '南宁市', '10000', '7e6ea2b730a9665c01dbcd4da25d113e', null, 'anaf', '1', '0', '0', null, null);

-- ----------------------------
-- Table structure for `sellers_order`
-- ----------------------------
DROP TABLE IF EXISTS `sellers_order`;
CREATE TABLE `sellers_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_id` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `visitor` int(11) DEFAULT NULL,
  `price` decimal(15,4) DEFAULT NULL,
  `order` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_sellers_order_seller_id` (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sellers_order
-- ----------------------------

-- ----------------------------
-- Table structure for `shipping`
-- ----------------------------
DROP TABLE IF EXISTS `shipping`;
CREATE TABLE `shipping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `max_price` decimal(10,2) DEFAULT NULL,
  `freight` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shipping
-- ----------------------------
INSERT INTO shipping VALUES ('1', '1', '默认配送', '等待配送员提货送货', '30.00', '3.00');

-- ----------------------------
-- Table structure for `special`
-- ----------------------------
DROP TABLE IF EXISTS `special`;
CREATE TABLE `special` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of special
-- ----------------------------

-- ----------------------------
-- Table structure for `special_products`
-- ----------------------------
DROP TABLE IF EXISTS `special_products`;
CREATE TABLE `special_products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `special_id` int(11) DEFAULT NULL,
  `products_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of special_products
-- ----------------------------

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_md5` varchar(32) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `unionid_md5` varchar(32) DEFAULT NULL,
  `unionid` varchar(8) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `birthday` varchar(100) DEFAULT NULL,
  `address_map` varchar(100) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `actualName` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `last_time` datetime DEFAULT NULL,
  `seller` int(11) DEFAULT '0',
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail` (`mail`),
  UNIQUE KEY `ix_users_phone` (`phone`),
  UNIQUE KEY `ix_users_username` (`username`),
  UNIQUE KEY `ix_users_unionid` (`unionid`),
  UNIQUE KEY `ix_users_id_md5` (`id_md5`),
  UNIQUE KEY `ix_users_unionid_md5` (`unionid_md5`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO users VALUES ('1', 'c4ca4238a0b923820dcc509a6f75849b', 'admin', '88312213c3492c4cd89d297f16cb0fc4', '12345678', 'pbkdf2:sha1:1000$XTWI2TdL$288636a24beddf14cdcc9d38d3ff7545534731ff', '1', null, null, '6471750@qq.com', '傻傻逼', '18977771077', '2017-02-17 09:55:07', '2017-02-17 09:55:07', '1', '1');
INSERT INTO users VALUES ('3', 'defac44447b57f152d14f30cea7a73cb', 'test', 'defac44447b57f152d14f30cea7a73cb', '12345679', 'pbkdf2:sha1:1000$EiVEp3QL$b649a66ee18eb001815c98566214940dc4cae343', '1', null, null, '6471751@qq.com', '大傻逼', '18977771078', '2017-02-27 10:06:52', '2017-02-27 10:06:52', '0', '1');
INSERT INTO users VALUES ('14', 'aab3238922bcc25a6f606eb525ffdc56', '100001', 'ca549c4218ce51cad24198d67b2f714a', '20325366', 'pbkdf2:sha1:1000$vuHHmKV3$4365c44921aded40dbde88dfc7901eaa58ed55af', '1', null, null, null, null, '3456', '2017-03-03 04:17:32', '2017-03-03 04:17:32', '0', '1');
