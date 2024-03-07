import SideNav from '@/components/side-nav'

export default function HomeLayout({ children }) {
	return (
		<div className='flex-1 flex'>
			<div className='flex-1 grid grid-cols-[minmax(4rem,_10rem)_minmax(39rem,_1fr)]'>
				<SideNav />
				{children}
			</div>
		</div>
	)
}
