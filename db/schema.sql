-- create database if not exists blink;

drop table if exists `blog`;
create table `blog` (
  `id` int not null auto_increment,
  `title` varchar(200) not null comment '标题',
  `content` text not null comment '内容',
  `created` timestamp default current_timestamp comment '创建时间',
  `updated` timestamp default current_timestamp on update current_timestamp comment '更新时间',
  primary key (`id`),
  key `ix_updated` (`updated`)
) engine=innodb default charset=utf8 comment='Blog主体表';

drop table if exists `tag`;
create table `tag` (
  `id` int not null auto_increment,
  `name` varchar(200) not null comment '名称',
  `created` timestamp default current_timestamp comment '创建时间',
  `updated` timestamp default current_timestamp on update current_timestamp comment '更新时间',
  primary key (`id`),
  key `ix_updated` (`updated`)
) engine=innodb default charset=utf8 comment='Tag主体表';

drop table if exists `blog_tag`;
create table `blog_tag` (
  `blog_id` int not null comment 'blog外键',
  `tag_id` int not null comment 'tag外键',
  CONSTRAINT `blog_ibfk_id` foreign key (`blog_id`) references blog(`id`),
  CONSTRAINT `tag_ibfk_id` foreign key (`tag_id`) references tag(`id`)
) engine=innodb default charset=utf8 comment='Blog~Tag M2M 关系映射表';
